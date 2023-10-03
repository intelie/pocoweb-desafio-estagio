import { useEffect, useState } from "react";

export function useMakeRequest<ResponseType>(url: string) {
  const [data, setData] = useState<ResponseType | undefined>();
  const [error, setError] = useState<unknown | undefined>(undefined);

  useEffect(() => {
    request<ResponseType>(url)
      .then((d) => setData(d))
      .catch((e) => setError(e));
  }, [url]);

  return { data, error };
}

export async function request<ResponseType>(url: string) {
  try {
    const response = await fetch(url);

    if (response.status >= 300) {
      throw response;
    }

    return (await response.json()) as ResponseType;
  } catch (error) {
    const errorMessage = { message: "Erro ao buscar dados", detail: error };
    if (error instanceof Response) {
      const data = await error.json();
      errorMessage.detail = data;
    }

    console.error(errorMessage);

    throw errorMessage;
  }
}
