console.log("js test");
// var equipmentDataUrl = "{% url 'cms:equipment_data' %}";
var $equipos = $('#equipos');

let equipoid = 0;

console.log($equipos);
console.log($equipos.data('url'));
$(document).ready(function () {
  var table = $('#equipos').DataTable({
    "ajax": {
      "url": "/cms/equipment-data/",  // Specify the relative URL here
      "type": "GET"
    },
    "processing": $equipos.data('processing'),
    "serverSide": $equipos.data('server-side'),
    "columns": [
      { "data": "id" },
      { "data": "equipo" },
      { "data": "marca" },
      { "data": "modelo" },
      { "data": "no_serie" },
      { "data": "servicio_ult" },
      { "data": "servicio_prox" },
      { "data": "estado" },
      { "data": "area" },
      { "data": "subarea" },
      { "data": "encargado" },

    ],
    "order": [[1, 'asc']],
    "paging": false,
    "ordering": true,
    "info": false,
    "filter": false,
  });
  $('#nuevo-btn').hide();
  $('#actualizar-btn').hide();

  $('#equipos tbody').on('click', 'tr', function (e) {
    // Check if the click target is an edit or delete button
    if (e.target.id === 'edit-btn' || e.target.id === 'delete-btn') {
      return; // Ignore the event for edit and delete buttons
    }

    var equipmentId = table.row(this).data().id;
    var equipo = table.row(this).data().equipo;
    var marca = table.row(this).data().marca;
    var modelo = table.row(this).data().modelo;
    var no_serie = table.row(this).data().no_serie;
    var ult_servicio = table.row(this).data().servicio_ult;
    var prox_servicio = table.row(this).data().servicio_prox;
    var estado = table.row(this).data().estado;
    var area = table.row(this).data().area;
    var subarea = table.row(this).data().subarea;
    var encargado = table.row(this).data().encargado;

    equipoid = equipmentId;

    $('#id-equipo').text(equipmentId);
    $('#equipo').text(equipo);
    $('#marca').text(marca);
    $('#modelo').text(modelo);
    $('#no-serie').text(no_serie);
    $('#ult-servicio').text(ult_servicio);
    $('#prox-servicio').text(prox_servicio);
    $('#estado').text(estado);
    $('#area').text(area);
    $('#subarea').text(subarea);
    $('#encargado').text(encargado);
    var pageTop = document.getElementById("page-top");
    pageTop.scrollIntoView({ behavior: "smooth", block: "start" });

    console.log(equipo);
    console.log("tbody");
    resetVisualIndication();

    // Fetch the MedicalEquipmentDetails data using AJAX
    cardInfo(equipoid)

    // Add visual indication to the clicked row
    $(this).addClass('clicked');
  });
  // Handle edit button click event
  $(document).on('click', '#nuevo-btn', function (e) {
    e.preventDefault();
    console.log(equipoid);
    var id = equipoid;
    showAddModal(id);
    console.log('Edit button clicked for equipment ID:', id);
  });

  // Handle delete button click event
  $(document).on('click', '#delete-btn', function (e) {
    e.preventDefault();
    var equipmentId = $(this).data('equipment-id');
    // Use equipmentId to perform necessary actions, such as opening the delete modal
    // You can customize this based on your modal implementation
    console.log('Delete button clicked for equipment ID:', equipmentId);
  });
  $(document).on('click', '#new_equipment_btn', function (e) {
    e.preventDefault();
    var test = 0
    showModalajax(test);
    resetVisualIndication();



  });


  $('#equipos tbody').on('mouseenter', 'tr', function () {
    $(this).addClass('hover');
  }).on('mouseleave', 'tr', function () {
    $(this).removeClass('hover');
  });




  function showAddModal(equipmentId) {
    $.ajax({
      url: '/cms/equipment_details_modal/' + equipmentId,
      type: 'GET',
      success: function (response) {
        resetVisualIndication();
        $('#agregar-modal .modal-body').html($(response).find('.modal-body').html());
        $('#agregar-modal').modal('show');
        console.log(equipmentId);
  
  
        $('#agregar-modal form').on('submit', function (e) {
          e.preventDefault();
  
          var formData = $(this).serialize();
  
          $.ajax({
            url:'/cms/equipment_details_modal/' + equipmentId,
            type: 'POST',
            data:  formData + '&equipo=' + equipmentId,
            success: function (response) {
              $('#agregar-modal').modal('hide');
              console.log(response);
              console.log($(this).attr('action'));
              console.log($(this).attr('method'));
              console.log(equipmentId);
              cardInfo(equipmentId);
            },
            error: function (xhr, status, error) {
              // Handle error
              console.error(error);
              console.error(status);
              console.error(xhr);
            }
          });
        });
      }
    });
  
    resetVisualIndication();
  }
  function showEditModal(equipmentId) {
    console.log('Modal opened for equipment ID:', equipmentId);
    resetVisualIndication();
    $('#editar-modal').modal('show');
    $('#editar-modall').on('hidden.bs.modal', function () {
    });
  }

  // Function to reset visual indication
  function resetVisualIndication() {
    $('#equipos tbody tr.clicked').removeClass('clicked');
  }

  function cardInfo(equipmentId){
    $.ajax({
      url: '/cms/equipment_details_view/' + equipmentId,
      success: function (data) {
        console.log(data);
        // Update the fields with the fetched data or placeholder values
        $('#inst-fecha').text(data.instalacion_fecha || 'N/A');
        $('#operando').text(data.anios_operando || 'N/A');
        $('#ult-actualizacion').text(data.ultima_actualizacion || 'N/A');
        $('#estatus').text(data.estatus || 'N/A');
        $('#ubicacion').text(data.ubicacion || 'N/A');
        $('#sububicacion').text(data.sub_ubicacion || 'N/A');
        $('#pertenencia').text(data.pertenencia || 'N/A');
        $('#duenio').text(data.duenio || 'N/A');
        $('#vendido-por').text(data.vendido_por || 'N/A');
        $('#adquisicion').text(data.adquisicion || 'N/A');
        $('#precio-compra').text(data.precio_compra || 'N/A');
        $('#divisas').text(data.divisas || 'N/A');
        $('#frecuencia_mprev').text(data.frecuencia_mprev || 'N/A');
        $('#ultimo-mprev').text(data.ultimo_mprev || 'N/A');
        $('#proximo-mprev').text(data.proximo_mprev || 'N/A');
        $('#riesgo').text(data.riesgo || 'N/A');
        $('#cricticidad').text(data.cricticidad || 'N/A');
        $('#provedor').text(data.garantia || 'N/A');
        $('#accesorios').text(data.accesorios || 'N/A');
        $('#garantia').text(data.garantia || 'N/A');
        // Update other fields similarly
        $('#nuevo-btn').show();
      },
      error: function () {
        // Display placeholder values for fields when there is no data available

      }
    });
  }
});
