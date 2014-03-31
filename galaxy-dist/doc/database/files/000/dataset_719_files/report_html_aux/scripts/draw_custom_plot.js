// Function that populates a data table,
// instantiates the column chart, passes in the data and
// draws it.
function drawColumnChart() {
	if(document.getElementById("ddl1").value == ''){alert('Select from dropdown menu');return;}
	var json = JSON.parse(document.getElementById('total-report-json').innerHTML);
	// Create the data table.
       var data = new google.visualization.DataTable();
       data.addColumn('string', 'Assembler');
       data.addColumn('number', document.getElementById('ddl1').value);
 	for(var x=0; x<json.report.length; x++){
		for(var y=1; y<json.report[x].length; y++){
			for(var z=0; z<json.report[x][y].length; z++){
				if(json.report[x][y][z].metricName == document.getElementById("ddl1").value){
					for(var i=0; i<json.report[x][y][z].values.length; i++){
						data.addRow([json.assembliesNames[i], json.report[x][y][z].values[i]]);
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

	var json = JSON.parse(document.getElementById('total-report-json').innerHTML);
	// Create the data table.
       var data = new google.visualization.DataTable();
       data.addColumn('number', document.getElementById('ddl2').value);
       data.addColumn('number', document.getElementById('ddl3').value);
	data.addColumn({type: 'string', role: 'tooltip'});
	var ddl2Val = null;
	var ddl3Val = null;
 	for(var x=0; x<json.report.length; x++){
		for(var y=1; y<json.report[x].length; y++){
			for(var z=0; z<json.report[x][y].length; z++){
				alert(json.report[x][y][z].metricName);
				if(json.report[x][y][z].metricName == document.getElementById("ddl2").value){
					ddl2Val = json.report[x][y][z].values;
					alert('ddl2 '+ddl2Val);
					if(document.getElementById("ddl2").value == document.getElementById("ddl3").value){
						ddl3Val = json.report[x][y][z].values;
						alert('Same value');
					}
				}
				else if(json.report[x][y][z].metricName == document.getElementById("ddl3").value){
					ddl3Val = json.report[x][y][z].values;
					alert('ddl3 '+ddl3Val);
				}
				if((ddl2Val != null) && (ddl3Val != null)){
					for(var i=0; i<ddl2Val.length; i++){
						var tooltip = json.assembliesNames[i]+'\n'+ddl2Val[i]+','+ddl3Val[i];
						data.addRow([ddl2Val[i], ddl3Val[i], tooltip]);
					}
					//data.addRow([Velvet, Abyss]);//json.assembliesNames]);
					//data.addRow([156,180]);//ddl2Val]);
					//data.addRow([349,100]);//ddl3Val]);
					alert('options');
				       // Set chart options
        				var options = {'title':'Scatterplot of '+document.getElementById("ddl2").value+' AND '+document.getElementById("ddl3").value,
							//'bar': {groupWidth: "90%"},
							hAxis: {title: document.getElementById("ddl2").value},
							vAxis: {title: document.getElementById("ddl3").value},
							crosshair: { trigger: 'both' },   // Display crosshairs.
							legend: 'none',
							//tooltip: { trigger: 'selection' }, // Display tooltips on selection.
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