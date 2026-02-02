import { routes } from "../main";

export const isAuthenticated = () => {
    const userData = localStorage.getItem("userData");
    return userData && JSON.parse(userData).isActive;
};

export function checkRouteAccess(pathname) {
    const dataInfo = JSON.parse(localStorage.getItem("userData")) || {};
    const isLoggedIn = isAuthenticated();
    const route = routes[pathname];

    if (!route && dataInfo.role === "User") return isLoggedIn ? "/events" : "/login";
    if (!route && dataInfo.role === "Admin") return isLoggedIn ? "/dashboard" : "/login";
    if (route && route.private && !isLoggedIn) return "/login";
    if (pathname === "/login" && isLoggedIn && dataInfo.role === "User") return "/events";
    if (pathname === "/login" && isLoggedIn && dataInfo.role === "Admin") return "/dashboard";

    return pathname;
}