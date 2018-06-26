interface IPost {
  images: IImage[];
  title?: string;
  url?: string;
}

interface IImage {
  base64: string;
  description?: string;
}