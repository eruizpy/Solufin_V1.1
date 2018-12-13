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