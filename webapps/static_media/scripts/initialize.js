function disableclick(e)
{
    if(event.button==2)
    {
        status="Context menus are disabled on purpose.";    
        alert(status);
        return false;	
    }
    return true;
}

document.onmousedown=disableclick;
