$(document).on('click', '#miModal', function(e){
    e.preventDefault();
	var sector = document.getElementById("id_SectorEconomico");
	var strSector = sector.options[sector.selectedIndex].text;
    $('#sector').val(strSector);
    return false;
});