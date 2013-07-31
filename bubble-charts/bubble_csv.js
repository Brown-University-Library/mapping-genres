var r = 960,
     format = d3.format(",d"),
     fill = d3.scale.category20c();
 
 var bubble = d3.layout.pack()
     .sort(null)
     .size([r, r]);
 
 var vis = d3.select("#chart").append("svg")
     .attr("width", r)
     .attr("height", r)
     .attr("class", "bubble");

 
 d3.csv("../data/AASCleanGenreDataTotals.csv", function(rows) {
   var node = vis.selectAll("g.node")
       .data(bubble.nodes(genres(rows))
       .filter(function(d) {return !d.children;}))
     .enter().append("g")
       .attr("class", "node")
       .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

   node.append("title")
       .text(function(d) { return d.cleanGenre + ": " + format(d.value); });
 
   node.append("circle")
       .attr("r", function(d) { return d.r; })
       .style("fill", function(d) { return fill(d.basicGenre); });
  
   node.append("text")
       .attr("text-anchor", "middle")
       .attr("dy", ".3em")
       .text(function(d) { return d.cleanGenre.substring(0, d.r / 3); });
 });
 
 function genres(rows) {
    return {children: rows}
 }