var curr_year = JSJoda.LocalDate.now()._year;
var light = true;

function getWeekNumber(date=null){
    if(date == null){
        return JSJodaExtra.YearWeek.now()._week;
    }else{
        return JSJodaExtra.YearWeek.from(JSJoda.LocalDate.parse(date))._week;
    }
}

function getWeekLetter(date=null){
    result = "";
    var count = getWeekNumber(date);
    var alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                 "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
    var index = (count-1) % 26;
    var result = alpha[index];
    if( count == 53 ){
        result = "-";
    }
    return result;
}

function getExampleCaseNames(date=null){
    if(date == null){
        date = JSJoda.LocalDate.now();
    }
    weekCount = getWeekNumber();
    weekLetter = getWeekLetter();
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
        year = curr_year;
    }
    var date = JSJoda.LocalDate.parse( String(year-1) +"-12-24");
    //date.setFullYear(year-1);
    //move date to Monday
    var day_offset = JSJoda.DayOfWeek.from(date)._ordinal;
    date = date.minusDays(day_offset);
    result = ""
    for(i=0;i<55;i++){
        month = JSJoda.Month.from(date)._name;
        month = month.charAt(0) + month.slice(1).toLowerCase();
        var str =
                "<tr><td class='text-center'>" + getWeekNumber(date.toString()) +
                "</td><td>" +  month +" "+ date._day +" "+ date._year +
                "</td><td class='fw-bold'>" + getWeekLetter(date.toString()) +
                "</td></tr>\n";
        result += str;
        date = date.plusWeeks(1);
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
        curr_year = JSJoda.LocalDate.now()._year;;
    }
    document.getElementById("wk_table").innerHTML = makeTable(curr_year);
    document.getElementById("year").innerHTML = curr_year;
}

function fillData(){
    var d = new JSJoda.LocalDate.now()
    var month = JSJoda.Month.from(d)._name;
    month = month.charAt(0) + month.slice(1).toLowerCase();
    var wk_day = d.dayOfWeek()._name;
    wk_day = wk_day.charAt(0) + wk_day.slice(1).toLowerCase();
    var full_date = wk_day+" "+month+" "+d._day+", "+d._year;

    document.getElementById("wk_number").innerHTML = getWeekNumber();
    document.getElementById("wk_letter").innerHTML = getWeekLetter();
    document.getElementById("label_a").innerHTML = getExampleCaseNames()[0];
    document.getElementById("label_b").innerHTML = getExampleCaseNames()[1];
    document.getElementById("year").innerHTML = curr_year;
    document.getElementById("date_today").innerHTML = full_date;
    document.getElementById("wk_table").innerHTML = makeTable();
}

function lights(){
    if( light ){
        light = false;
        document.documentElement.setAttribute("data-bs-theme", "dark");
        document.getElementById("page").classList.replace("bg-white", "bg-dark");
        document.getElementById("more_info").classList.replace("bg-light", "bg-secondary");
        document.getElementById("switcha").setAttribute("hidden", "")
        document.getElementById("switchb").removeAttribute("hidden")

    }else{
        light = true;
        document.documentElement.setAttribute("data-bs-theme", "");
        document.getElementById("page").classList.replace("bg-dark", "bg-white");
        document.getElementById("more_info").classList.replace("bg-secondary","bg-light");
        document.getElementById("switcha").removeAttribute("hidden")
        document.getElementById("switchb").setAttribute("hidden", "true")
    }
}
window.onload = function(){
    fillData();
}