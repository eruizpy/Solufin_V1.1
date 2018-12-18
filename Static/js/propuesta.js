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

$(function(){
    $('.add-row').click(function() {
        return addForm(this, 'cheque');
    });
    $('.delete-row').click(function(){
        return deleteForm(this, 'cheque');
    });
    $('.Emision').keypress(function(event){
        return AutoSlash(this ,event);
    });
})

function addForm(btn, prefix) {
    var formCount = parseInt($('#id_'+ prefix + '-TOTAL_FORMS').val());
    var row = $('.dynamic-form:first').clone(true).get(0);
    $(row).removeAttr('id').insertAfter($('.dynamic-form:last')).children('.hidden').removeClass('hidden');
    $(row).children().not(':last').children().each(function(){
        updateElementIndex(this, prefix, formCount);
        $(this).val('');
    });
    $(row).find('.delete-row').click(function(){
        deleteForm(this, prefix);
    });
    $('#id_'+ prefix +'-TOTAL_FORMS').val(formCount + 1);
    return false;
}

function updateElementIndex(el, prefix, ndx){
    var id_regex = new RegExp('(' + prefix + '-\\d+)');
    var replacement = prefix + '-' + ndx;
    if ($(el).attr("for")) $(el).attr("for", $(el).attr("for").replace(id_regex, replacement));
    if (el.id) el.id = el.id.replace(id_regex, replacement);
    if (el.name) el.name = el.name.replace(id_regex, replacement);
}

function deleteForm(btn, prefix) {
    $(btn).parents('.dynamic-form').remove();
    var forms = $('.dynamic-form');
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);
    for (var i=0, formCount=forms.length; i<formCount; i++) {
        $(forms.get(i)).children().not(':last').children().each(function() {
            updateElementIndex(this, prefix, i);
        });
    }
    return false;
}

function AutoSlash(data, event){
    if(event.which !== 8) { 
        var numChars = $(data).val().length;
        if(numChars === 2 || numChars === 5){
            var thisVal = $(data).val();
            thisVal += '/';
            $(data).val(thisVal);
        }
  }
}