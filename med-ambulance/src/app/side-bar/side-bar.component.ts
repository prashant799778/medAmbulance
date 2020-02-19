import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthsService } from '../services/auths.service';
declare var jQuery: any;

@Component({
  selector: 'app-side-bar',
  templateUrl: './side-bar.component.html',
  styleUrls: ['./side-bar.component.css']
})
export class SideBarComponent implements OnInit {

	constructor(public router:Router,public authsService: AuthsService) { }

	ngOnInit() {
	}

	goToPage(routes){
		this.router.navigateByUrl('/'+routes)
	}
	logout(){
   
		this.authsService.logout()
	}
	logouts(){
		jQuery('#logout-pop').modal('show')
	}
	closeModal(){
		jQuery('#logout-pop').modal('hide')
	}

}
