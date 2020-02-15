import { Component, OnInit } from '@angular/core';
import { AuthsService } from '../services/auths.service';
import { LocalStorageService } from 'angular-web-storage';
declare var jQuery: any;

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  userName: any;
  activatedds: boolean;
  constructor(public authsService: AuthsService,
             public local: LocalStorageService) {
                this.activatedds = false
              }

  ngOnInit() {
    if(this.local.get('userData1') && this.local.get('userData1')[0] && this.local.get('userData1')[0].userName){
      console.log(this.local.get('userData1')[0].userName)
      this.userName = this.local.get('userData1')[0].userName
    }
    
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