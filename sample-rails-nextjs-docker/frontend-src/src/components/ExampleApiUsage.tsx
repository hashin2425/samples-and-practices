'use client';

import { fetchFromApi, postToApi } from '../actions/api';

interface ExampleData {
  id: number;
  title: string;
}

interface CreateData {
  title: string;
}

export default function ExampleApiUsage() {
  // Example of using server action in a form submit
  async function handleSubmit(formData: FormData) {
    const title = formData.get('title') as string;
    const result = await postToApi<CreateData, ExampleData>('/api/examples', { title });

    if (result.error) {
      console.error('Error creating data:', result.error);
    } else {
      console.log('Created data:', result.data);
    }
  }

  // Example of using server action in a button click
  async function handleFetch() {
    const result = await fetchFromApi<ExampleData[]>('/api/examples');

    if (result.error) {
      console.error('Error fetching data:', result.error);
    } else {
      console.log('Fetched data:', result.data);
    }
  }

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">API Usage Example</h1>

      {/* Example form using server action */}
      <form action={handleSubmit} className="mb-4">
        <input type="text" name="title" placeholder="Enter title" className="border p-2 mr-2" />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2 rounded">
          Create
        </button>
      </form>

      {/* Example button using server action */}
      <button onClick={handleFetch} className="bg-green-500 text-white px-4 py-2 rounded">
        Fetch Data
      </button>
    </div>
  );
}
