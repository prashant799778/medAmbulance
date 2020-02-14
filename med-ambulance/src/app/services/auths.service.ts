
import { Injectable, Output, EventEmitter, Inject, ElementRef, Renderer } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

import { Observable, Subject } from 'rxjs';
import { map, catchError, share } from 'rxjs/operators';

// import { IUserLogin } from '../../shared/services/interfaces';
// import { UserService } from './user.service';
import { LocalStorageService, SessionStorageService, LocalStorage, SessionStorage } from 'angular-web-storage';
import { Router } from '@angular/router';
import { UserService } from './user.service';
declare var jQuery: any
// import { LoginComponent } from '../component/account/login.component';
// import { AuthService } from 'angularx-social-login';
// import { VotingComponent } from '../../campaigns/voting/voting.component'

@Injectable({
  providedIn: 'root'
})
export class AuthsService {

    // port = (this.window.location.port) ? ':' + this.window.location.port : '';
    // baseUrl = `${this.window.location.protocol}//${this.window.location.hostname}${this.port}`;
    // authUrl = this.baseUrl + '/api/auth';
    baseUrl= 'http://134.209.153.34:5031/';
    // baseUrl = `http://139.59.78.54:5021/`;
    isAuthenticated = false;
    loginSuccess: number;
    loginSuccesss: number;
    redirectUrl: string;
    href: any;
    KEY = 'value';
    online: number;
    isCheckedLogin: any;
    superAdminLogin: boolean;
    logoutEvent = new EventEmitter<any>();
    private onSubject = new Subject<{ key: string, value: any }>();
    public changes = this.onSubject.asObservable().pipe(share());
    @Output() authChanged: EventEmitter<boolean> = new EventEmitter<boolean>();


  constructor(private http: HttpClient,
              public session: SessionStorageService,
              public userService: UserService,
              public local: LocalStorageService,
              public router: Router,
              
              ) {
                
              
              this.start();
            
              // this.storageEventListener.bind(this)
              
             
                this.loginSuccesss = 0;
               }

  private userAuthChanged(status: boolean) {
    console.log(status)
    // if(status == true){
      this.authChanged.emit(status); // Raise changed event
    // }
    
  }
  private start(): void {
    window.addEventListener("storage", this.storageEventListener.bind(this));
}
  private storageEventListener(event: StorageEvent) {
    // console.log(event.storageArea , localStorage)
    if (event.storageArea == localStorage) {
        let v;
        try {
            v = JSON.parse(event.newValue);
        } catch (e) {
            v = event.newValue;
        }
        this.onSubject.next({key: event.key, value: v});
    }
   

  }

  public getStorage() {
    let s = [];
    for (let i = 0; i < localStorage.length; i++) {
        s.push({
            key: localStorage.key(i),
            value: JSON.parse(localStorage.getItem(localStorage.key(i)))
        });
    }
    return s;
}

  
  login(userLogin): Observable<boolean> {
    console.log(userLogin);
    return this.http.get<boolean>(this.baseUrl + 'Login'+'?email='+userLogin.email+'&password='+userLogin.password )
        .pipe(
            map(loggedIn => {
                let resp;
                resp = loggedIn;
                if(resp.status == 'true'){
                  this.loginCondition(resp)
                  if(resp.result.userTypeId == 1){
                    console.log('hello super login')
                    this.superAdminLogin = true;
                    
                  }else{
                    console.log('hello super login false')
                    this.superAdminLogin = false;
                  }
                  // this.userService.setSuperLogin(this.superAdminLogin)
                

                }
                else{
                  this.loginSuccess = 0;
                  this.loginSuccesss = 0;
                  // this.userAuthChanged(resp.status);
                }

               
                return loggedIn;
            }),
            catchError(this.handleError)
        );
  }

  logout(){
    console.log("logout step 1 --------")
    
    console.log("logout step 2 --------")
    this.session.clear();
    console.log("logout step 3 --------")
    this.local.clear();
    console.log("logout step 4 --------")
    console.log("logout ",this.local)
    this.loginSuccess = 0;
    console.log("logout step 5 --------")
    this.isAuthenticated = false;
    this.loginSuccesss = 0;
    
    this.userAuthChanged(false);
    this.href = this.router.url;
    jQuery("#logout-pop").modal('hide')
    this.router.navigateByUrl('/dashboard')
    this.logoutEvent.emit()
    
    
    
   
    // window.location.reload();
   
  }
  

  private handleError(error: HttpErrorResponse) {
    console.error('server error:', error);
    if (error.error instanceof Error) {
      const errMessage = error.error.message;
      return Observable.throw(errMessage);
      
    }
    return Observable.throw(error || 'Server error');
  }

  socialLogin(data){
      
    return  new Promise((resolve, reject) => {
      
      this.http.post(this.baseUrl+'SocialMediaLogin',data).toPromise().then(
        res => { // Success
          let resp;
                resp = res;
                
          if(resp.status == 'true'){
          this.loginCondition(resp);
          resolve(resp)

           }
           else{
            reject('error')
             this.loginSuccess = 0;
             this.loginSuccesss = 0;
             this.userAuthChanged(resp.status);
           }
        }
      );
  });
  }

  loginCondition(resp){

    this.isAuthenticated = resp.status;
    this.loginSuccess = 1;
    this.loginSuccesss = 1
    console.log(resp)
    this.userAuthChanged(resp.status);
    // this.userService.getSaveCustomer(resp['result'][0]);
   
    let userIIId = resp.result;
   
    this.href = this.router.url;
   
    let charhref = this.href.split('?');
 
    if(charhref[0] == '/campaign/voting'){
      let id = charhref[1].split('=')
     
      let campId = id[1].split('&')
      console.log(campId)
     
      
      // this.userService.getCampaignss(campId[0],userIIId[0].UserId)
    }
    
  }
}




