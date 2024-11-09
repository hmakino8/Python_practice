import axios from "axios";

// Fetch all lists
export const fetchLists = async () => {
  try {
    const response = await axios.get("http://localhost:8000/api/list/");
    console.log("Lists:", response.data);
    return response.data;
  } catch (error) {
    console.error("Error fetching lists:", error);
  }
};

// Create a new list
export const createList = async (newList) => {
  try {
    const response = await axios.post(
      "http://localhost:8000/api/list/",
      newList
    );
    console.log("List created:", response.data);
  } catch (error) {
    console.error("Error creating list:", error);
  }
};

// Update a list
export const updateList = async (listId, updatedData) => {
  try {
    const response = await axios.put(
      `http://localhost:8000/api/list/${listId}/`,
      updatedData
    );
    console.log("List updated:", response.data);
  } catch (error) {
    console.error("Error updating list:", error);
  }
};

// Delete a list
export const deleteList = async (listId) => {
  try {
    await axios.delete(`http://localhost:8000/api/list/${listId}/`);
    console.log("List deleted");
  } catch (error) {
    console.error("Error deleting list:", error);
  }
};
