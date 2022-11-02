$(document).ready(() => {
    getFeedback();
})

function getFeedback() {
    $.ajax({
        type: "GET",
        url: "/json-all/"
    }).done((data) => {
        putFeedback(data);
    });
}

function putFeedback(data) {
  const cardContainer = $('#allFeedback');
  cardContainer.empty();
  data.forEach(task => {
      const taskCard = `
      <li class="card">
        <div>
          <h6 class="card-title">RATING: ${task.fields.rating}/10</h6>
          <h6 class="card-subtitle mb-2 text-muted">${task.fields.date}</h6>
          <div class="card-content">
          <span>
            <p>Feedback: </p>
            <p class="feedback"> ${task.fields.feedback}</p>
          </span>
          </div>
        </div>
      </li>
      `
      cardContainer.append(taskCard);
    })
};