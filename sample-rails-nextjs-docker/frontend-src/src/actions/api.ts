'use server';

interface ApiResponse<T> {
  data: T | null;
  error: string | null;
}

// Generic GET request function
export async function fetchFromApi<T>(endpoint: string): Promise<ApiResponse<T>> {
  try {
    const response = await fetch(`http://localhost:3001${endpoint}`, {
      cache: 'no-store', // Disable caching to always get fresh data
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return { data, error: null };
  } catch (error) {
    return {
      data: null,
      error: error instanceof Error ? error.message : 'An unknown error occurred',
    };
  }
}

// Generic POST request function
export async function postToApi<T, U>(endpoint: string, body: T): Promise<ApiResponse<U>> {
  try {
    const response = await fetch(`http://localhost:3001${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      cache: 'no-store',
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return { data, error: null };
  } catch (error) {
    return {
      data: null,
      error: error instanceof Error ? error.message : 'An unknown error occurred',
    };
  }
}

// Generic PUT request function
export async function putToApi<T, U>(endpoint: string, body: T): Promise<ApiResponse<U>> {
  try {
    const response = await fetch(`http://localhost:3001${endpoint}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
      cache: 'no-store',
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return { data, error: null };
  } catch (error) {
    return {
      data: null,
      error: error instanceof Error ? error.message : 'An unknown error occurred',
    };
  }
}

// Generic DELETE request function
export async function deleteFromApi<T>(endpoint: string): Promise<ApiResponse<T>> {
  try {
    const response = await fetch(`http://localhost:3001${endpoint}`, {
      method: 'DELETE',
      cache: 'no-store',
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    const data = await response.json();
    return { data, error: null };
  } catch (error) {
    return {
      data: null,
      error: error instanceof Error ? error.message : 'An unknown error occurred',
    };
  }
}
