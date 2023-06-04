// Function to clear the previous results
function clearResults() {
    const headerList = document.getElementById('header-list');
    headerList.innerHTML = '';
  }
  
  // Function to display the results
  function displayResults(headers) {
    const headerList = document.getElementById('header-list');
    headerList.innerHTML = '';
  
    Object.entries(headers).forEach(([name, value]) => {
      const lines = value.split('\n');
      const listItem = document.createElement('li');
      listItem.className = 'header-item';
  
      const headerName = document.createElement('span');
      headerName.innerHTML = `${name}:`;
      // Set text color based on the condition
      if (name.includes('Missing')) {
        headerName.style.color = 'red';
      } else {
        headerName.style.color = 'green';
      }
      listItem.appendChild(headerName);
  
      lines.forEach((line, index) => {
        const lineItem = document.createElement('div');
        lineItem.innerHTML = line;
        listItem.appendChild(lineItem);
  
        // Add an additional line gap after each line
        if (index !== lines.length - 1) {
          const lineGap = document.createElement('div');
          lineGap.innerHTML = '&nbsp;';
          listItem.appendChild(lineGap);
        }
      });
  
      headerList.appendChild(listItem);
    });
  
    const resultContainer = document.getElementById('result-container');
    resultContainer.style.display = 'block';
  }
  
  
  
  
  // Function to handle the search button click
  function handleSearch() {
    const urlInput = document.getElementById('url-input');
    const url = urlInput.value.trim();
  
    if (url !== '') {
      clearResults();
  
      fetch('https://techzon.pythonanywhere.com/check_headers', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ url })
      })
        .then(response => response.json())
        .then(data => displayResults(data.headers))
        .catch(error => console.log(error));
    }
  }
  
  // Attach the search button click event listener
  document.getElementById('search-btn').addEventListener('click', handleSearch);
  