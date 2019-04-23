function sendBackend() {
  let content = document.getElementById('val').value;
  let data = {
    'content': content
  };

  let req = {
    method: "POST",
    mode: "cors",
    cache: "no-cache",
    credentials: "same-origin",
    headers: {
      "Content-Type": "application/json",
    },
    redirect: "follow",
    referrer: "no-referrer",
    body: JSON.stringify(data),
  }

  fetch('/receive_json', req)
    .then((res) => {
      res.json()
        .then((res_json) => {
          if (res_json['method'] === "json_sent") {
            document.getElementById('res').innerHTML = res_json['data'];
          }
        });
    });
}

function addEventListeners() {
  document.getElementById('submit').addEventListener('click', sendBackend);
}

addEventListeners();
