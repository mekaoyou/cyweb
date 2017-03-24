/**
处理业务数据的js
*/

function commandHandler(command)
{
	console.log("处理业务数据的js command处理前 -> "+command);
	console.log("处理业务数据的js command处理后 -> "+splitCommand(command));

	var result = "";
	$.ajax({
		type:"get",
		async:false,
		url: splitCommand(command),
		data:{},
		dataType:"json",
		success:function(data){
			console.log("get success -> " + data);
			result = data.name
		},
		error:function(data){
			console.log("get error -> " + data);
			result = "No such command!"
		}
	});

    return result;
}

function splitCommand(command)
{
	var commandArr = command.trim().replace(/&nbsp;/g, " ").replace(/\s+/g," ").trim().split(" ");
	if(commandArr.length > 1)
	{
		return "/"+commandArr.join("/")+"/";
	}
	return command.trim();
}