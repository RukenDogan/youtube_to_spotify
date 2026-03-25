import { z } from "zod";

export const youtubeSchema = z.object({
  youtube_url: z
    .string()
    .trim()
    .min(1, "Veuillez entrer une URL")
    .refine(
      (value) =>
        value.includes("youtube.com") && value.includes("list="),
      {
        message: "URL de playlist YouTube invalide",
      }
    ),
});