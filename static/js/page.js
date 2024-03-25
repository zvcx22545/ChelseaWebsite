document.addEventListener("DOMContentLoaded", function () {
  const scheduleHeader = document.getElementById("news");
  const scheduleLink = document.querySelector(".menu a[href='#news']");

  let isScheduleClicked = false;
  let isResultsClicked = false;

  scheduleLink.addEventListener("click", function (event) {
    // event.preventDefault();
    if (!isScheduleClicked) {
      scheduleHeader.style.marginTop = "10rem";
      isScheduleClicked = true;
      isResultsClicked = false;
    } else {
      scheduleHeader.style.marginTop = "0";
      isScheduleClicked = false;
    }
  });

  resultsLink.addEventListener("click", function (event) {
    // event.preventDefault();
    if (!isResultsClicked) {
      resultsHeader.style.marginTop = "10rem";
      isResultsClicked = true;
      isScheduleClicked = false;
    } else {
      resultsHeader.style.marginTop = "0";
      isResultsClicked = false;
    }
  });
});
