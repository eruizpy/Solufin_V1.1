$('#OperacionForm').on('keyup keypress', function(e) {
    var keyCode = e.keyCode || e.which;
        if (keyCode === 13) { 
        e.preventDefault();
        return false;
    }
});
document.getElementById('id_NroCliente').onkeydown = function(event) {
    if (event.keyCode == 13) {
        var numero = $("#id_NroCliente").val();
        $.ajax({
        	type: "GET",
        	url: "/ajax/get_cliente/",
        	data: {
        		'numero': numero
        	},
        	success: function(response){
        		if(response.NoMatch){
        			$("#getModal1").modal('show');
        			$('#id_NombreCliente').val('');
        			$('#id_SectorEconomico').val('');
    	    		$('#id_Telefono').val('');
	        		$('#id_DireccionLibre').val('');
        		}else{
        			$('#id_NombreCliente').val(response.nombre);
        			$('#id_SectorEconomico').val(response.sector);
    	    		$('#id_Telefono').val(response.telefono);
	        		$('#id_DireccionLibre').val(response.direccion);
        		}
        	},
        });
    }
}

document.getElementById('id_NroAgente').onkeydown = function(event) {
    if (event.keyCode == 13) {
        var numero = $("#id_NroAgente").val();
        $.ajax({
            type: "GET",
            url: "/ajax/get_agente/",
            data: {
                'numero': numero
            },
            success: function(response){
                if(response.NoMatch){
                    $('#id_NombreAgente').val('');
                    $("#getModal2").modal('show');
                }else{
                    $('#id_NombreAgente').val(response.nombre);
                }
            },
        });
    }
}