async function fetchWeather() {
  const location = document.getElementById("location").value.trim();
  const resultDiv = document.getElementById("weather-result");

  if (!location) {
    resultDiv.innerHTML = `<div class="alert alert-warning">Please enter a location.</div>`;
    return;
  }

  try {
    const res = await axios.post("/api/weather", { location });
    const data = res.data;

    let html = `<h5>${data.location}</h5><table class="table table-sm">
                  <thead><tr><th>Date</th><th>Max</th><th>Min</th><th>Rain %</th></tr></thead><tbody>`;
    data.days.forEach(d => {
      html += `<tr><td>${d.date}</td><td>${d.maxtemp}°C</td><td>${d.mintemp}°C</td><td>${d.rain}%</td></tr>`;
    });
    html += "</tbody></table>";

    resultDiv.innerHTML = html;
  } catch (err) {
    resultDiv.innerHTML = `<div class="alert alert-danger">Error: ${err.response?.data?.error || err.message}</div>`;
  }
}

async function generatePassword() {
  let length = parseInt(document.getElementById("length").value);
  const resultDiv = document.getElementById("password-result");

  // validação do número
  if (isNaN(length) || length < 1) length = 1;
  if (length > 1000) length = 1000;

  try {
    const res = await axios.post("/api/password", { length });
    resultDiv.textContent = res.data.password;
    resultDiv.classList.remove("d-none");
  } catch (err) {
    resultDiv.textContent = `Error: ${err.response?.data?.error || err.message}`;
    resultDiv.classList.remove("d-none");
  }
}
