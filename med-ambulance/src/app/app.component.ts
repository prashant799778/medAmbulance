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
	superAdmin: boolean;
	location
	subAdmin: boolean;
	pastbook: boolean;
	
	constructor(public local: LocalStorageService,public authsService: AuthsService,public userService: UserService){
		// this.local.get('userData1')
		this.location = window.location.origin
		console.log(this.location)
		// if(this.location == 'http://localhost:4201'){
		// 	this.subAdmin = true;

		// }else{
		// 	this.subAdmin = false;
		// }
		setTimeout(()=>{
			if(this.local.get('userData1') && this.local.get('userData1').userTypeId){
				console.log("if lougout",this.local.get('userData1').userTypeId)
				this.loginSuccessfull = true;
				if(this.local.get('userData1').userTypeId == 1){
					this.superAdmin = true;
					console.log('checkkkkkkkk111111')
				}else{
					this.superAdmin = false;
					console.log('checkkkkkkkk222222')
				}
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

		this.userService.pastBook.subscribe(()=>{
			console.log('event true')
			this.pastbook = true;
		})
		this.userService.pastBooks.subscribe(()=>{
			console.log('event true')
			this.pastbook = false;
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
		if(dataName == 'Hospital'){
			let data = {
				'id': this.userService.deletDataId
			}
			this.userService.dataPostApi(data,AppSettings.deleteHospital).then(resp=>{
				if(resp['status'] == 'true'){
					this.activatedds = true;
					this.userService.EmitEvnt(dataName);
					
					setTimeout(()=>{
						jQuery('#deleteModal').modal('hide')
					},2000)
				}
			})
		}
		if(dataName == 'Hospital Admin'){
			let data = {
				'Id': this.userService.deletDataId
			}
			this.userService.dataPostApi(data,AppSettings.deletehospitalAdmin).then(resp=>{
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
