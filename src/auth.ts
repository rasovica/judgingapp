import * as AWS from "aws-sdk";
import { apiUrl, identityPoolId, region } from "@/constants";
import * as aws4 from "aws4";

AWS.config.region = region;

const cognitoIdentity = new AWS.CognitoIdentity();

function createAnonymousUser() {
  return new Promise((resolve, reject) => {
    cognitoIdentity.getId(
      { IdentityPoolId: identityPoolId },
      (err: any, data: any) => {
        if (err) {
          return reject(err);
        }

        AWS.config.credentials = new AWS.CognitoIdentityCredentials({
          IdentityPoolId: identityPoolId,
          IdentityId: data.IdentityId
        });

        if ("expired" in AWS.config.credentials) {
          AWS.config.credentials.refresh(err => {
            if (err) {
              reject(err);
            }
            console.log(AWS.config.credentials);
          });
        }

        return resolve(data.IdentityId);
      }
    );
  });
}

async function signRequest(
  path: string,
  method = "GET",
  host = apiUrl,
  service = "execute-api"
) {
  const request = {
    host,
    path,
    method,
    service,
    url: host + path
  };

  console.log("THIS IS THE REQUEST", request);

  if (!AWS.config.credentials) {
    await createAnonymousUser().catch(console.error);
  }

  if (AWS.config.credentials && "expired" in AWS.config.credentials) {
    if (AWS.config.credentials.expired) {
      AWS.config.credentials.refresh(err => {
        console.log(err);
      });
    }

    console.log("THIS ARE THE CREDENTIALS", AWS.config.credentials);

    const signedRequest = aws4.sign(request, {
      secretAccessKey: AWS.config.credentials.secretAccessKey,
      accessKeyId: AWS.config.credentials.accessKeyId,
      sessionToken: AWS.config.credentials.sessionToken
    });

    delete signedRequest.headers.Host;
    delete signedRequest.headers["Content-Length"];

    return signedRequest;
  }
}

export { createAnonymousUser, signRequest };
