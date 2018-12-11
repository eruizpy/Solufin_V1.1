//Put our input DOM element into a jQuery Object
var $jqDate = jQuery('input[id="id_FechaNacimiento"]');

//Bind keyup/keydown to the input
$jqDate.bind('keyup','keydown', function(e){
	
  //To accomdate for backspacing, we detect which key was pressed - if backspace, do nothing:
	if(e.which !== 8) {	
		var numChars = $jqDate.val().length;
		if(numChars === 2 || numChars === 5){
			var thisVal = $jqDate.val();
			thisVal += '/';
			$jqDate.val(thisVal);
		}
  }
});

// Apellido + Nombre = Nombre Completo
$(document).ready(function(){
    $("#id_PrimerApellido").on("focusout", getNombreCompleto);
    $("#id_PrimerNombre").on("focusout", getNombreCompleto);
});

function getNombreCompleto(){
	var apellido = $("#id_PrimerApellido").val();
	var nombre = $("#id_PrimerNombre").val();
	var nombre_completo = nombre+" "+apellido;
	$("#id_NombreCompleto").siblings('label, i').addClass('active');
	$("#id_NombreCompleto").val(nombre_completo);
}