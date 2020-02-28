import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthsService } from '../services/auths.service';
import { LocalStorageService } from 'angular-web-storage';
import { UserService } from '../services/user.service';
declare var jQuery: any;

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.css']
})
export class SideBarComponent implements OnInit {
	locations: any;
	secondLocation: any;
	subAdmin: boolean;

	constructor(public router:Router,public authsService: AuthsService,public userService:UserService,
				public local: LocalStorageService) { }

	ngOnInit() {
		if(this.local.get('userData1') && this.local.get('userData1').userTypeId && this.local.get('userData1').userTypeId == 5){
			this.subAdmin = true;
		}else{
			this.subAdmin = false;
			this.locations = window.location.href
			this.secondLocation = this.locations.substring(0, this.locations.lastIndexOf("/") + 1)
			this.locations = this.locations.substring(this.locations.lastIndexOf("/") + 1, this.locations.length );
			this.secondLocation = this.secondLocation.substring(this.secondLocation.lastIndexOf("/") + 1, this.secondLocation.length - 5 );
			console.log(this.locations)
			console.log(this.secondLocation)
			if(this.locations == 'allHospital'){
				setTimeout(()=>{
					jQuery(".left-menu li").removeClass('active');
					var elem = document.getElementById('hospital');
					elem.click()
					jQuery("#allHospital").addClass("active")
				},100)
			}else if(this.locations == 'addHospital'){
				setTimeout(()=>{
					jQuery(".left-menu li").removeClass('active');
					var elem = document.getElementById('hospital');
					elem.click()
					jQuery("#addHospital").addClass("active")
				},100)
			}else if(this.locations == 'allPassengers'){
				setTimeout(()=>{
					jQuery(".left-menu li").removeClass('active');
					jQuery("#allPassengers").addClass("active")
				},100)
			}else if(this.locations == 'bookedTrip'){
				setTimeout(()=>{
					jQuery(".left-menu li").removeClass('active');
					var elem = document.getElementById('tripId');
					elem.click()
					jQuery("#tripIdB").addClass("active")
				},100)
			}else if(this.locations == 'completeTrip'){
				setTimeout(()=>{
					jQuery(".left-menu li").removeClass('active');
					var elem = document.getElementById('tripId');
					elem.click()
					jQuery("#tripIdC").addClass("active")
				},100)
			}else if(this.locations == 'activeTrip'){
				setTimeout(()=>{
					jQuery(".left-menu li").removeClass('active');
					var elem = document.getElementById('tripId');
					elem.click()
					jQuery("#tripIdA").addClass("active")
				},100)
			}else if(this.locations == 'cancelTrip'){
				setTimeout(()=>{
					jQuery(".left-menu li").removeClass('active');
					var elem = document.getElementById('tripId');
					elem.click()
					jQuery("#tripIdCa").addClass("active")
				},150)
			}


		}
	}

	goToPage(routes){
		this.router.navigateByUrl('/'+routes)
	}
	logout(){
   
		this.authsService.logout()
	}
	logouts(){
		jQuery('#logoutModal').modal('show')
	}
	closeModal(){
		jQuery('#logoutModal').modal('hide')
	}
	pastBookingOPen(){
		this.userService.pastBookOpen()
	}
	pastBookingOPens(){
		this.userService.pastBookOpens()
	}

}
