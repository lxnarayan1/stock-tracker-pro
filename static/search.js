console.log("search.js loaded ");

const input = document.getElementById("search-input");
const suggestionsList = document.getElementById("suggestions-list");

if (input) {
  input.addEventListener("input", async () => {
    const query = input.value.trim();
    if (!query) {
      suggestionsList.innerHTML = "";
      return;
    }

    try {
      const response = await fetch(`/autocomplete/?q=${query}`);
      const suggestions = await response.json();

      suggestionsList.innerHTML = "";
      suggestions.forEach(item => {
        const li = document.createElement("li");
        li.textContent = `${item.symbol} - ${item.name}`;
        li.addEventListener("click", () => {
          input.value = item.symbol; // fill input
          suggestionsList.innerHTML = ""; // clear dropdown
        });
        suggestionsList.appendChild(li);
      });
    } catch (error) {
      console.error("Error fetching suggestions:", error);
    }
  });
}

// Clear suggestions when clicking outside
document.addEventListener("click", (event) => {
  if (!input.contains(event.target) && !suggestionsList.contains(event.target)) {
    suggestionsList.innerHTML = "";
  }
});
