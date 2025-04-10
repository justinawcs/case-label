// This function provided by EpochConverter.com
// see https://www.epochconverter.com/weeknumbers
Date.prototype.getWeek = function () {
    var target  = new Date(this.valueOf());
    var dayNr   = (this.getDay() + 6) % 7;
    target.setDate(target.getDate() - dayNr + 3);
    var firstThursday = target.valueOf();
    target.setMonth(0, 1);
    if (target.getDay() != 4) {
        target.setMonth(0, 1 + ((4 - target.getDay()) + 7) % 7);
    }
    return 1 + Math.ceil((firstThursday - target) / 604800000);
}

var curr_year = new Date().getFullYear();

Date.prototype.getWeekLetter = function(){
    var target = new Date(this.valueOf());
    var count = target.getWeek();
    var alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    var index = count % 26;
    var result = alpha[index-1];
    if( Math.trunc(count) == 53){
        result = "-";
    }
    return result;
}

function getExampleCaseNames(date=null){
    if(date == null){
        date = new Date();
    }
    weekCount = date.getWeek();
    weekLetter = date.getWeekLetter();
    result = ["E+_##X","Z+_##X"];
    if(weekCount <= 26){
        result[0] = result[0].replace("+", "B");
        result[1] = result[1].replace("+", "B");
    }else{
        result[0] = result[0].replace("+", "E");
        result[1] = result[1].replace("+", "Z");
    }
    result[0] = result[0].replace("_", weekLetter);
    result[1] = result[1].replace("_", weekLetter);
    return result;
}

function makeTable(year=null){
    if(year == null){
        year = new Date().getFullYear();
    }
    date = new Date( String(year-1) +"-12-24");
    //date.setFullYear(year-1);
    //move date to Monday
    date.setDate(date.getDate() - date.getDay() );
    result = ""
    for(i=0;i<56;i++){
        var split_date = date.toUTCString().split(" ")
        var str = "<tr><td>" +  split_date[2] +" "+ split_date[1] +" "+ split_date[3] +
                  "</td><td>" + date.getWeek() +
                  "</td><td>" + date.getWeekLetter() +
                  "</td></tr>\n";
        result += str;
        //result += "date +" "+ date.getWeek() +" "+ date.getWeekLetter() +"\n";
        date.setDate(date.getDate() + 7);
    }
    return result;
}

function changeTable(action){
    if(action == "prev"){
        curr_year -= 1;
    }
    if(action == "next"){
        curr_year += 1;
    }
    if(action == null){
        curr_year = new Date().getFullYear();
    }
    document.getElementById("wk_table").innerHTML = makeTable(curr_year);
    document.getElementById("year").innerHTML = curr_year;
}

function fillData(){
    d = new Date()
    document.getElementById("wk_number").innerHTML = d.getWeek();
    document.getElementById("wk_letter").innerHTML = d.getWeekLetter();
    document.getElementById("label_a").innerHTML = getExampleCaseNames()[0];
    document.getElementById("label_b").innerHTML = getExampleCaseNames()[1];
    document.getElementById("year").innerHTML = curr_year;
    document.getElementById("wk_table").innerHTML = makeTable();
}

window.onload = function(){
    fillData();
}