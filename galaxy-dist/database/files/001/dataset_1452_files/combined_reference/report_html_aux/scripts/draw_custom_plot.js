// Function that populates a data table,
// instantiates the column chart, passes in the data and
// draws it.
function drawColumnChart() {
    if(document.getElementById("ddl1").value == ''){alert('Select from dropdown menu');return;}
    var json = JSON.parse(document.getElementById('total-report-json').textContent);
    // Create the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Assembler');
    data.addColumn('number', document.getElementById('ddl1').value);
    for(var x=0; x<json.report.length; x++){
	for(var y=1; y<json.report[x].length; y++){
	    for(var z=0; z<json.report[x][y].length; z++){
		if(json.report[x][y][z].metricName == document.getElementById("ddl1").value){
		    for(var i=0; i<json.report[x][y][z].values.length; i++){
			if (json.report[x][y][z].values[i].length != 0){
			    data.addRow([json.assembliesNames[i], json.report[x][y][z].values[i]]);
			}
		    }
		    // Set chart options
		    var options = {'title':'Barchart of '+document.getElementById('ddl1').value,
				   'legend': {position: 'none'},
				   'width':700,
				   'height':600};
		    // Instantiate and draw our chart, passing in some options.
		    var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
		    chart.draw(data, options);
		    document.getElementById('chart_div').style.display = 'block';
		    document.getElementById('hideplot').style.display = 'block';
		    x=json.report.length;
		    y=json.report[x].length;
		    z=json.report[x][y].length;
		}
	    }
	}
    }
}

// Function that populates a data table,
// instantiates the scatter plot, passes in the data and
// draws it.
function drawScatterPlot() {
    if(document.getElementById("ddl2").value == '' || document.getElementById("ddl3").value == ''){alert('Select from both dropdown menus');return;}

    var json = JSON.parse(document.getElementById('total-report-json').textContent);
    // Create the data table.
    var data = new google.visualization.DataTable();
    data.addColumn('number', 'X-value');

    var ddl2Val = null;
    var ddl3Val = null;
    for(var x=0; x<json.report.length; x++){
	for(var y=1; y<json.report[x].length; y++){
	    for(var z=0; z<json.report[x][y].length; z++){
		if(json.report[x][y][z].metricName == document.getElementById("ddl2").value){
		    ddl2Val = json.report[x][y][z].values;
		    if(document.getElementById("ddl2").value == document.getElementById("ddl3").value){
			ddl3Val = json.report[x][y][z].values;
		    }
		}
		else if(json.report[x][y][z].metricName == document.getElementById("ddl3").value){
		    ddl3Val = json.report[x][y][z].values;
		}
		if((ddl2Val != null) && (ddl3Val != null)){
		    var len = ddl2Val.length;
		    var asmNames = json.assembliesNames;
		    for(var g=0; g<len; g++){
			if((ddl2Val[g].length != 0) && (ddl3Val[g].length != 0)){
			    if(ddl2Val[g].toString().indexOf('+') > -1){
				ddl2Val[g] = ddl2Val[g].split(' + ')[0];
			    }
			    if(ddl3Val[g].toString().indexOf('+') > -1){
				ddl3Val[g] = ddl3Val[g].split(' + ')[0];
			    }
			}else{
			    ddl2Val.splice(g, 1);
			    if(document.getElementById("ddl2").value != document.getElementById("ddl3").value){
				ddl3Val.splice(g, 1);
			    }
			    asmNames.splice(g, 1);
			    len -= 1;
			    g -= 1;
			}
		    }
		    for(var i=0; i<asmNames.length; i++){
			data.addColumn('number', asmNames[i]);
		    }
		    data.addRows(ddl2Val.length);    
		    for(var i=0; i<ddl2Val.length; i++){
			data.setCell(i,0,ddl2Val[i]);
			data.setCell(i,i+1,ddl3Val[i]);
		    }
		    // Set chart options
		    var options = {'title':'Scatterplot of '+document.getElementById("ddl2").value+' AND '+document.getElementById("ddl3").value,
				   'hAxis': {title: document.getElementById("ddl2").value},
				   'vAxis': {title: document.getElementById("ddl3").value},
				   'crosshair': {trigger: 'both' },   // Display crosshairs.
				   'width':700,
				   'height':600};
		    // Instantiate and draw our chart, passing in some options.
		    var chart = new google.visualization.ScatterChart(document.getElementById('chart_div'));
		    chart.draw(data, options);
		    document.getElementById('chart_div').style.display = 'block';
		    document.getElementById('hideplot').style.display = 'block';
		    x=json.report.length;
		    y=json.report[x].length;
		    z=json.report[x][y].length;
		    
		}
	    }
	}
    }
}

function toggleImg(){
    document.getElementById('chart_div').style.display = 'none';
    document.getElementById('hideplot').style.display = 'none';
}