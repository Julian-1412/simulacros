import { adminDashboardLogic } from "./dashboard.js";
import { adminEventsLogic } from "./eventManage.js";
import { userEventsLogic } from "./events.js";
import { loginLogic } from "./loginLogic.js";
import { myRegistrationsLogic } from "./myEvents.js";
import { registUserLogic } from "./userRegist";
import { userManagmentLogic } from "./userRender";

export function initViewLogic(path) {

    if (path === "/login") {
        loginLogic();
    } 
    else if (path === "/registration") {
        registUserLogic();
    } 
    else if (path === "/usermanagment") {
        userManagmentLogic();
    } 
    else if (path === "/events") {
        userEventsLogic();
    } 
    else if (path === "/my-events") {
        myRegistrationsLogic();
    }
    else if(path === "/eventManagement") {
        adminEventsLogic();
    }
    else if(path === "/dashboard") {
        adminDashboardLogic();
    }
}