import { Component } from '@angular/core';
import { LocalStorageService } from 'angular-web-storage';
import { AuthsService } from './services/auths.service';
import { UserService } from './services/user.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
	title = 'med-ambulance';
	loginSuccessfull: boolean;
	constructor(public local: LocalStorageService,public authsService: AuthsService,public userService: UserService){
		// this.local.get('userData1')
		setTimeout(()=>{
			if(this.local.get('userData1') && this.local.get('userData1').userTypeId){
				console.log("if lougout")
				this.loginSuccessfull = true;
			}else{
				console.log("else lougout",this.local.get('userData1'))
				this.loginSuccessfull = false;
			}
		},500)
		
		this.authsService.logoutEvent.subscribe(()=>{
			console.log()
			this.loginSuccessfull = false;
		})
		this.authsService.loginEvent.subscribe(()=>{
			this.loginSuccessfull = true;
		})
		
	}
}
