document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('#form').onsubmit = () => {
    // Initialize new request
    const request = new XMLHttpRequest();
    const currency = document.querySelector('#currency').value;
    request.open('POST', '/convert');
    request.onload = () => {
      // Extract JSON data from response
      const data = JSON.parse(request.responseText);
      // Output the result to div id="result"
      if (data.success) {
        const contents = `1 USD is equal to ${data.rate} ${currency}`;
        document.querySelector('#result').innerHTML = contents;
      } else {
        document.querySelector('#result').innerHTML = "There was an error occured.";
      }
    };
    // Add data to send with request
    const data = new FormData();
    data.append('currency', currency);
    request.send(data);
    // Prevent reloading page
    return false
  };
});
