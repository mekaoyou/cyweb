/**
处理业务数据的js
*/
var QUERY_COMMAND = "query";
var DETAIL_COMMAND = "detail";
var CATEGORY_COMMAND = "cate";
var ARTICLE_COMMAND = "art";
var ARTICLE_LIST_COMMAND = "arts";
var WELLCOME_COMMAND = "wellcome";

function commandHandler(input_str)
{
	console.log("处理业务数据的js command处理前 -> "+input_str);
	console.log("处理业务数据的js command处理后 -> "+getURL(input_str));

	var url = getURL(input_str);
	var command = getCommand(url);

	var result = "";
	$.ajax({
		type:"get",
		async:false,
		url: url,
		data:{},
		dataType:"json",
		success:function(data){
			result = switchCommand(command, $.parseJSON(data))
		},
		error:function(data){
			console.log("get error -> " + data);
			result = "No such command!"
		}
	});

    return result;
}

function getURL(command)
{
	var commandArr = command.trim()
							.replace(/&nbsp;+/g, " ")
							.replace(/\s+/g," ")
							.replace(/<br>+/g," ")
							.trim()
							.split(" ");
	if(commandArr.length > 1)
	{
		return "/"+commandArr.join("/")+"/";
	}
	return command.trim();
}

function getCommand(url)
{
	return url.replace(/\//g, " ").trim().split(" ")[0];
}

function switchCommand(command, data)
{
	console.log(command);
	switch(command)
	{
		case QUERY_COMMAND:
			return handleQueryResult(data);
		case DETAIL_COMMAND:
			return handleDetailResult(data);
		case CATEGORY_COMMAND:
			return handleCateGoryResult(data);
		case ARTICLE_COMMAND:
			return handleArtResult(data);
		case ARTICLE_LIST_COMMAND:
			return handleArtsResult(data);
		case WELLCOME_COMMAND:
			return handleWellComeResult(data);
		default:
			return "No such command!";
	}
}

function handleWellComeResult(json)
{
	if(json[0] != null && json[0] != undefined)
	{
		return json[0].fields.wellcome;
	}
	return "Well Come to Shell Blog!<br>Powered by Alex"
}

function handleArtsResult(json)
{
	var artList_html = "<table>";
    $.each(json, function(index, obj){
        //console.log(obj.fields.name);
        artList_html += "<tr><td>"+obj.pk+"&nbsp;&nbsp;</td><td>"+obj.fields.title+"</td></tr>"
    });
    artList_html += "</table>";
    artList_html += "<br>共检索到 " + json.length + " 条记录";
    if(json.length > 0)
    {
    	artList_html += '<br>tips:你可以使用 "art <文章ID>" 命令查看文章详情';
    }
    return artList_html;
}

function handleArtResult(json)
{
	var art_html = "<table>"
	if(json.length > 0)
	{
		data = json[0].fields;
		console.log(data);
		art_html += "<tr><td>"+data.title+"</td></tr>"
		art_html += "<tr><td>作者: "+data.auth+"&nbsp;&nbsp;&nbsp;"+new Date(data.date_time).Format("yyyy-MM-dd")+"</td></tr>"
		art_html += "<tr><td>分类: "+data.category+"</td></tr>"
		art_html += "<tr><td>"+data.content+"</td></tr>"
	}
	else
	{
		art_html += "<tr><td>文章不存在</td></tr>"
	}
	art_html += "</table>"
	return art_html;
}

function handleCateGoryResult(json)
{
	var isBlog = 0;
	var catList_html = "<table>"
	$.each(json, function(index, obj){
		if(obj.fields.name == undefined)
		{
			isBlog = 1
			catList_html += "<tr><td>"+obj.pk+"&nbsp;&nbsp;</td><td>"+obj.fields.title+"</td></tr>"
		}
		else
		{
			catList_html += "<tr><td>"+obj.pk+"&nbsp;&nbsp;</td><td>"+obj.fields.name+"</td></tr>"
		}
	});
	catList_html += "</table>";

	return catList_html;
}

function handleQueryResult(json)
{
	var cyList_html = "<table>";
    $.each(json, function(index, obj){
        //console.log(obj.fields.name);
        cyList_html += "<tr><td>"+obj.pk+"&nbsp;&nbsp;</td><td>"+obj.fields.name+"</td></tr>"
    });
    cyList_html += "</table>";
    cyList_html += "<br>共检索到 " + json.length + " 条记录";
    if(json.length > 0)
    {
    	cyList_html += '<br>tips:你可以使用 "detail <成语ID or 成语名>" 命令查看成语详情';
    }
    return cyList_html;
}

function handleDetailResult(data)
{
	var detail_html = "<table>"
	if(data.length > 0)
	{
		data = data[0].fields;
		detail_html += "<tr><td colspan=2>"+data.name+"</td></tr>"
		detail_html += "<tr><td colspan=2>"+data.spell+"</td></tr>"
		detail_html += "<tr><td>释义&nbsp;->&nbsp;</td><td>"+data.content+"</td></tr>"
		detail_html += "<tr><td>出处&nbsp;->&nbsp;</td><td>"+data.derivation+"</td></tr>"
		detail_html += "<tr><td>举例&nbsp;->&nbsp;</td><td>"+data.samples+"</td></tr>"
	}
	else
	{
		detail_html += "<tr><td>不存在此成语</td></tr>"
	}
	detail_html += "</table>"
	return detail_html;
}