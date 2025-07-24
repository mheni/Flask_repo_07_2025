const API_BASE = "/api/people";

function refreshTable() {
  $.get(API_BASE, function (data) {
    const table = $("#people-table");
    table.empty();
    data.forEach(person => {
      table.append(`
        <tr>
          <td>${person.fname}</td>
          <td>${person.lname}</td>
          <td>${person.timestamp}</td>
        </tr>
      `);
    });
  });
}

function showError(message) {
  $("#error-msg").text(message);
  setTimeout(() => $("#error-msg").text(""), 3000);
}

$("#create").click(function () {
  const fname = $("#fname").val();
  const lname = $("#lname").val();
  if (!fname || !lname) return showError("Both names are required");

  $.ajax({
    url: `${API_BASE}/${lname}`,
    type: "POST",
    contentType: "application/json",
    data: JSON.stringify({ fname, lname }),
    success: refreshTable,
    error: res => showError(res.responseJSON?.message || "Create failed")
  });
});

$("#update").click(function () {
  const fname = $("#fname").val();
  const lname = $("#lname").val();
  if (!lname) return showError("Last name is required");

  $.ajax({
    url: `${API_BASE}/${lname}`,
    type: "PUT",
    contentType: "application/json",
    data: JSON.stringify({ fname }),
    success: refreshTable,
    error: res => showError(res.responseJSON?.message || "Update failed")
  });
});

$("#delete").click(function () {
  const lname = $("#lname").val();
  if (!lname) return showError("Last name is required");

  $.ajax({
    url: `${API_BASE}/${lname}`,
    type: "DELETE",
    success: refreshTable,
    error: res => showError(res.responseJSON?.message || "Delete failed")
  });
});

$("#reset").click(function () {
  $("#fname").val("");
  $("#lname").val("");
});

$(document).ready(refreshTable);
