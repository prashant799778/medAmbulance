import { Injectable } from '@angular/core';
import { Router, CanActivate, CanActivateChild, CanLoad, Route, UrlSegment, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { SessionStorageService, LocalStorageService } from 'angular-web-storage';
import { AuthsService } from './auths.service';
import { UserService } from './user.service';
import { splitClasses } from '@angular/compiler';
// import { UserServicervice } from './user.service';
// import { SessionStorageService } from 'angular-web-storage';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate, CanActivateChild, CanLoad {
  KEY = 'value';
  constructor(
    private router: Router,
    
    public session: SessionStorageService,
    public local: LocalStorageService,
    public authservice: AuthsService,
    public userService: UserService,
    // private authenticationService: AuthenticationService
) { }
  canActivate(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      console.log(this.local)
      console.log(window.location.href)
      let location = window.location.href
      location = location = location.substring(location.lastIndexOf("/") + 1, location.length );
      let secondLocation = location.substring(0, location.lastIndexOf("/") + 1)
      secondLocation = secondLocation.substring(secondLocation.lastIndexOf("/") + 1, secondLocation.length - 5 );
      console.log(location)
      let splitLocation = location.split('?')
      console.log(splitLocation[0])
      if( splitLocation[0] == 'AccountVerification'){
        // this.router.navigateByUrl('/AccountVerification')
        console.log("success")
      }else{
        if (this.session.get(this.KEY)) {
          let isuserLoggedIn = this.local.get('userData1');
         
         
          this.userService.getSaveCustomer(isuserLoggedIn);
          let isuserLoggedIn1 = this.local.get('userData2');
         
         
          this.userService.getSaveCustomer1(isuserLoggedIn1);
          return true;
      }else{
        console.log(this.local.get('userData1'))
        let isuserLoggedIn = this.local.get('userData1');
        
        this.userService.getSaveCustomer(isuserLoggedIn);
        let isuserLoggedIn1 = this.local.get('userData2');
         
         
          this.userService.getSaveCustomer1(isuserLoggedIn1);
        
        return true;
      }
      }
      

    
    
  
     



   
  }
  canActivateChild(
    next: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      // this.session
    return true;
  }
  canLoad(
    route: Route,
    segments: UrlSegment[]): Observable<boolean> | Promise<boolean> | boolean {
    return true;
  }
}
