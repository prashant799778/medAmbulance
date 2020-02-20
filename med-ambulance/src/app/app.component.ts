import { Component, EventEmitter } from '@angular/core';
import { LocalStorageService } from 'angular-web-storage';
import { AuthsService } from './services/auths.service';
import { UserService } from './services/user.service';
import { AppSettings } from './utils/constant';
declare var jQuery: any;
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
	title = 'med-ambulance';
	loginSuccessfull: boolean;
	activatedds: boolean;
	
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
	logout(){
   
		this.authsService.logout()
		jQuery('#logoutModal').modal('hide')
	  }

	closeModal(){
		jQuery('#logoutModal').modal('hide')
	}
	zoomOut(){
		jQuery('#zoomImageModal').modal('hide')
	}
	deleteData(dataName){
		console.log(dataName)
		if(dataName == 'Driver'){
			let data = {
				'driverId': this.userService.deletDataId
			}
			this.userService.dataPostApi(data,AppSettings.deleteDriver).then(resp=>{
				if(resp['status'] == 'true'){
					this.activatedds = true;
					this.userService.EmitEvnt(dataName);
					
					setTimeout(()=>{
						jQuery('#deleteModal').modal('hide')
					},2000)
				}
			})
		}
	}
}
