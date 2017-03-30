$(document).ready(function(){

	var $divText = $("#textDiv");
	var _WELL_COME_MSG = "Well come to Web Shell site! <br>"
						+"Powered by Alex <br>"
						+"2017-2-23 <br>"
						+"------------------------------------------------<br>";
	var _WEB_SHELL = "Web Shell~$";
	var _WEB_SHELL_NEXTLINE = "<br>" + _WEB_SHELL;

	var _DIR_KEYS = [33,34,35,36,37,38,39,40];

	var _HISTORY_COMMAND = [];
	var _CURRENT_COMMAND_INDEX = 0;

	var _DEFAULT_COMMAND_HELP = "help";
	var _DEFAULT_COMMAND_CLEAR = "clear";
	var _DEFAULT_COMMAND_DATE = "date";

	var _DEFAULT_COMMANDS =
		[
		_DEFAULT_COMMAND_HELP,
		_DEFAULT_COMMAND_CLEAR,
		_DEFAULT_COMMAND_DATE,
		]

	$(this).keydown(function(e){
		//console.log(e.keyCode);
		if(isSelectMore() || isOnUneditArea())
		{
			if(!(e.ctrlKey && (e.keyCode == 67 || e.keyCode == 116))
				&& !(e.shiftKey && (_DIR_KEYS.indexOf(e.keyCode) != -1))
				&& e.keyCode != 116
				&& _DIR_KEYS.indexOf(e.keyCode) == -1)
			{
				if(e.keyCode == 38 || e.keyCode == 40){handleUpAndDown(e.keyCode);}
				return stop(e);
			}
		}

		if(e.keyCode == 13)
		{
			enterDown();
			return stop(e);
		}
		else if(e.keyCode == 8 || e.keyCode == 46)
		{
			if($divText.html().slice(-_WEB_SHELL.length) == _WEB_SHELL)
			{
				return stop(e);
			}
		}
		else if(e.keyCode == 38 || e.keyCode == 40)
		{
			handleUpAndDown(e.keyCode);
			return stop(e);
		}
		else
		{
		}
	});

	function stop(e)
	{
		e.stopPropagation();
		return false;
	}

	/**判断当前光标是否在不可编辑区域（当前命令行以上均视为不可编辑）*/
	function isOnUneditArea()
	{
		var startContainer = "";
		var startOffset = -1;
		if (window.getSelection || document.getSelection)
	 	{
	 		//chrome,firefox,opera
	        var range=window.getSelection().getRangeAt(0);
	        startContainer = range.startContainer.nodeValue;
	        startOffset = range.startOffset;
	    }
	    var input_command = getInputCommand();
	    /*console.log("startContainer -> "+ startContainer);
	    console.log("_WEB_SHELL -> "+ _WEB_SHELL);
	    console.log("getInputCommand() -> "+ input_command);
	    console.log("startContainer.length -> "+ (startContainer != null?startContainer.length:null));
	    console.log("startOffset -> "+ startOffset);*/
	    if(startContainer == null){return false;}
	    if(startContainer == input_command){return false;}

	    if(startContainer == _WEB_SHELL && startOffset >= startContainer.length){return false;}
	    if(startContainer != _WEB_SHELL && startContainer != input_command)
	    {
	    	if(startContainer.indexOf(_WEB_SHELL) == -1){return false;}
	    	else if(startContainer.indexOf(_WEB_SHELL) != -1
	    			&& startOffset >= _WEB_SHELL.length){return false;}
	    }
	    return true;
	}

	function handleUpAndDown(keyCode)
	{
		if(_HISTORY_COMMAND.length <= 0){return;}
		//console.log(_HISTORY_COMMAND.join(","));
		if(keyCode == 38)
		{
			if(_CURRENT_COMMAND_INDEX > 0)
			{
				clearCurrentInput();
				_CURRENT_COMMAND_INDEX--;
				//console.log(_CURRENT_COMMAND_INDEX);
				appendText(_HISTORY_COMMAND[_CURRENT_COMMAND_INDEX])
			}
		}
		else
		{
			if(_CURRENT_COMMAND_INDEX < _HISTORY_COMMAND.length-2)
			{
				clearCurrentInput();
				_CURRENT_COMMAND_INDEX++;
				console.log(_CURRENT_COMMAND_INDEX);
				appendText(_HISTORY_COMMAND[_CURRENT_COMMAND_INDEX])
			}
		}
	}

	function clearCurrentInput()
	{
		var currentText = $divText.html()
		var currentTextArr = currentText.split(_WEB_SHELL);
		var currentInput = currentTextArr.pop()
		$divText.html("")
		appendText(currentText.substring(0, currentText.lastIndexOf(currentInput)))
	}

	$(this).mousedown(function(e){
		$divText.focus();
	});

	$(this).click(function(e){
		$divText.focus();
	});

	$(this).bind("contextmenu",function(e){
		return stop(e);
	})

	/**判断当前是否选中了多个文字*/
	function isSelectMore()
	{
		var selectText = "";
	 	if (window.getSelection || document.getSelection)
	 	{
	 		//chrome,firefox,opera
	        var range=window.getSelection().getRangeAt(0);
	        var container = document.createElement('div');
	        container.appendChild(range.cloneContents());
	        selectText = container.innerHTML;
	        //selectText = window.getSelection(); //只复制文本
	    }
	    else if (document.selection)
	    {
	    	//IE特有的
	        selectText = document.selection.createRange().htmlText;
	        //selectText = document.selection.createRange().text; //只复制文本
	    }
	    if(selectText.length > 1){ return true;}
	    return false;
	}


	function getInputCommand()
	{
		var currentText = $divText.html();
		var input_command_arr = currentText.split(_WEB_SHELL)
		var input_command = input_command_arr[input_command_arr.length-1]
		return input_command;
	}


	function enterDown()
	{
		input_command = getInputCommand();
		appendText(handleCommand(input_command))
		appendText(_WEB_SHELL_NEXTLINE)
	}

	function handleCommand(command)
	{
		if(command.trim() == ""){return command;}
		//console.log(command);
		_HISTORY_COMMAND.push(command);
		_CURRENT_COMMAND_INDEX = _HISTORY_COMMAND.length;

		var handleCommand = "";
		if(command == _DEFAULT_COMMAND_CLEAR)
		{
			$divText.text("");
			return handleCommand
		}
		else if(command == _DEFAULT_COMMAND_DATE)
		{
			handleCommand = new Date().Format(CURRENT_FORMAT);
		}
		else if(command == _DEFAULT_COMMAND_HELP)
		{
			handleCommand = _DEFAULT_COMMANDS.join("&nbsp;&nbsp;&nbsp;")
		}
		else
		{
			handleCommand = commandHandler(command);
		}

		return "<br><span style='color:red'>"+handleCommand+"</span>";
	}



	function appendText(text)
	{
		$divText.focus();

		if(window.getSelection && window.getSelection().getRangeAt)
		{
			var range, node;

			range = window.getSelection().getRangeAt(0);
			range.collapse(false);
			var currentText = $divText.html();
			$divText.text("");
			node = range.createContextualFragment(currentText + text);
			c = node.lastChild;
			range.insertNode(node);
			if(c)
			{
				range.setEndAfter(c);
				range.setStartAfter(c)
			}
			j = window.getSelection();
			j.removeAllRanges();
			j.addRange(range);
		}
		else if(document.selection && document.selection.createRange)
		{
			document.selection.createRange().pasteHTML(text);
		}
		//自动滚屏
		$("html,body").animate({scrollTop:$("#bottom").offset().top},0)
	}


	appendText(_WELL_COME_MSG);
	appendText(_WEB_SHELL);
});