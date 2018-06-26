import Amplify from "aws-amplify";
import { apiUrl, identityPoolId, region } from "@/constants";
import API from "aws-amplify/lib/API";

Amplify.configure({
  Auth: {
    identityPoolId,
    region,
    mandatorySignIn: false
  },
  API: {
    endpoints: [
      {
        name: "main",
        endpoint: apiUrl
      }
    ]
  }
});

async function new_post(title?: string) {
  return await API.post("main", "/post", {body: {title}});
}

export { new_post };
