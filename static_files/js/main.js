
const navigation = document.getElementById("nav");
const menu = document.getElementById("menu");

menu.addEventListener("click", () => {
  // The navigation.children.length means the following :-
  // The children inside a parent are basically an array of elements; So, here I'm finding the length of the array aka how many children are inside the nav bar.
  //   Yup That's all.
  navigation.style.setProperty("--childenNumber", navigation.children.length);

  //    Casually Toggling Classes to make them animate on click
  //   Regular stuff ;)
  navigation.classList.toggle("active");
  menu.classList.toggle("active");
});


$(document).ready(function () {
  if (!$.browser.webkit) {
    $('.wrapper').html('<p>Sorry! Non webkit users. :(</p>');
  }
});


document.addEventListener('DOMContentLoaded', function () {
  // Hide loading container initially
  document.getElementById('loading-container').style.display = 'none';

  // Add event listener to the download button
  document.getElementById('download-form').addEventListener('submit', function (event) {
    // Prevent the default form submission
    // event.preventDefault();

    // Show loading container when the button is clicked
    document.getElementById('loading-container').style.display = 'block';

    // Simulate an asynchronous function to fetch data (replace this with your actual data fetching logic)
    setTimeout(function () {
      // Hide loading container
      document.getElementById('loading-container').style.display = 'none';

      // Show content container
      document.getElementById('content-container').style.display = 'flex';

      // Submit the form programmatically (replace this with the actual form submission logic)
      // document.getElementById('download-form').submit();
    }, 3000); // Replace 3000 with the actual time it takes to fetch data
  });
});