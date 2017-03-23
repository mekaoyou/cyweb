/**
处理业务数据的js
*/

function commandHandler(command)
{
	var result = "";
	$.ajax({
		type:"get",
		async:false,
		url:"/"+command+"/",
		data:{},
		dataType:"json",
		success:function(data){
			result = data.name
		},
		error:function(data){
			result = "No such command!"
		}
	});

    return result;
}