/**
处理业务数据的js
*/
var QUERY_COMMAND = "query";
var DETAIL_COMMAND = "detail";

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
	var commandArr = command.trim().replace(/&nbsp;/g, " ").replace(/\s+/g," ").trim().split(" ");
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
	switch(command)
	{
		case QUERY_COMMAND:
			return handleQueryResult(data);
		case DETAIL_COMMAND:
			return handleDetailResult(data);
		default:
			return "No such command!";
	}
}

function handleQueryResult(json)
{
	var cyList_html = "<table>";
    $.each(json, function(index, obj){
        console.log(obj.fields.name);
        cyList_html += "<tr><td>"+obj.pk+"&nbsp;&nbsp;</td><td>"+obj.fields.name+"</td></tr>"
    });
    cyList_html += "</table>";
    cyList_html += "<br>共检索到 " + json.length + " 条记录";
    if(json.length > 0)
    {
    	cyList_html += "<br>你可以使用 detail <成语ID> 命令查看成语详情";
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