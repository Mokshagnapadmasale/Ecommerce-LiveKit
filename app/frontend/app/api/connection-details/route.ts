import { NextResponse } from "next/server";
import { v4 as uuidv4 } from "uuid";

type ConnectionDetails = {
  serverUrl: string;
  participantToken: string;
};

export const revalidate = 0;

export async function POST() {
  try {
    // Generate a unique user identity for this voice session
    const userId = uuidv4();

    // Ask FastAPI to generate a LiveKit token for this user
    const res = await fetch(
      `http://localhost:4000/token?user_id=${userId}`,
      { cache: "no-store" }
    );

    if (!res.ok) {
      throw new Error("Failed to get token from FastAPI");
    }

    const data = await res.json();

    // Send token + server URL back to LiveKit frontend
    return NextResponse.json(
      {
        serverUrl: data.url,
        participantToken: data.token,
      },
      {
        headers: { "Cache-Control": "no-store" },
      }
    );
  } catch (e: any) {
    console.error(e);
    return new NextResponse(e.message || "Internal Server Error", {
      status: 500,
    });
  }
}
