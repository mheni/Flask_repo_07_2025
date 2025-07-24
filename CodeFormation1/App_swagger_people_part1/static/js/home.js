$(document).ready(function () {
  const API_URL = "/api/people";

  // Fonction pour charger et afficher les personnes
  function loadPeople() {
    $.getJSON(API_URL)
      .done(function (data) {
        const tbody = $("tbody");
        tbody.empty();

        data.forEach(person => {
          const row = `
            <tr data-lname="${person.lname}">
              <td>${person.fname}</td>
              <td>${person.lname}</td>
              <td>${person.timestamp}</td>
            </tr>`;
          tbody.append(row);
        });

        $(".error").text(""); // Clear errors on success
      })
      .fail(function () {
        $(".error").text("Erreur de chargement des personnes.");
      });
  }

  // Reset les champs du formulaire et messages d'erreur
  $("#reset").click(function () {
    $("#fname").val("");
    $("#lname").val("");
    $(".error").text("");
  });

  // Créer une personne
  $("#create").click(function () {
    const fname = $("#fname").val().trim();
    const lname = $("#lname").val().trim();

    if (!fname || !lname) {
      $(".error").text("Veuillez remplir le prénom et le nom.");
      return;
    }

    $.ajax({
      url: `${API_URL}/${lname}`,
      method: "POST",
      contentType: "application/json",
      data: JSON.stringify({ fname }),
      success: function () {
        loadPeople();
        $("#reset").click();
      },
      error: function () {
        $(".error").text("Erreur lors de la création.");
      }
    });
  });

  // Mettre à jour une personne
  $("#update").click(function () {
    const fname = $("#fname").val().trim();
    const lname = $("#lname").val().trim();

    if (!fname || !lname) {
      $(".error").text("Veuillez remplir le prénom et le nom.");
      return;
    }

    $.ajax({
      url: `${API_URL}/${lname}`,
      method: "PUT",
      contentType: "application/json",
      data: JSON.stringify({ fname }),
      success: function () {
        loadPeople();
        $("#reset").click();
      },
      error: function () {
        $(".error").text("Erreur lors de la mise à jour.");
      }
    });
  });

  // Supprimer une personne
  $("#delete").click(function () {
    const lname = $("#lname").val().trim();

    if (!lname) {
      $(".error").text("Veuillez remplir le nom pour supprimer.");
      return;
    }

    $.ajax({
      url: `${API_URL}/${lname}`,
      method: "DELETE",
      success: function () {
        loadPeople();
        $("#reset").click();
      },
      error: function () {
        $(".error").text("Erreur lors de la suppression.");
      }
    });
  });

  // Cliquer sur une ligne pour remplir le formulaire
  $("tbody").on("click", "tr", function () {
    const fname = $(this).find("td:eq(0)").text();
    const lname = $(this).find("td:eq(1)").text();

    $("#fname").val(fname);
    $("#lname").val(lname);
    $(".error").text("");
  });

  // Charger la liste au chargement de la page
  loadPeople();
});
