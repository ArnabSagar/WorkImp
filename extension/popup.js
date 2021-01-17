var list = document.getElementById('list');

function updateList() {
  var url = document.getElementById("textarea").value;
  document.getElementById('textarea').innerHTML = url;
  var entry = document.createElement('li');
  entry.appendChild(document.createTextNode(url));
  list.appendChild(entry);
}
