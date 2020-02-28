import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClient, HTTP_INTERCEPTORS }    from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MyDatePickerModule } from 'mydatepicker';
import { NgSelectModule } from '@ng-select/ng-select';
import { NgZorroAntdModule } from 'ng-zorro-antd';
// import { NgxMqttClientModule } from 'ngx-mqtt-client';
// import { MqttModule, IMqttServiceOptions } from "ngx-mqtt";
// import { Observable } from 'rxjs';
import { AgmCoreModule } from '@agm/core';
import { AgmDirectionModule } from 'agm-direction';

import { Observable } from 'rxjs';

import {
  IMqttMessage,
  MqttModule,
  IMqttServiceOptions
} from 'ngx-mqtt';

export const MQTT_SERVICE_OPTIONS: IMqttServiceOptions = {
  hostname: '134.209.153.34',
  port: 8083,
  path: ''
};


import { AppComponent } from './app.component';
import { AccountComponent } from './account/account.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { HeaderComponent } from './header/header.component';
import { SideBarComponent } from './side-bar/side-bar.component';

import { ActiveTripComponent } from './trip/active-trip/active-trip.component';
import { CompleteTripComponent } from './trip/complete-trip/complete-trip.component';
import { BookedTripComponent } from './trip/booked-trip/booked-trip.component';
import { RouteMapComponent } from './trip/route-map/route-map.component';
import { TripSharedComponent } from './trip/trip-shared/trip-shared.component';
import { AddDriverComponent } from './driver/add-driver/add-driver.component';
import { AllDriverComponent } from './driver/all-driver/all-driver.component';
import { DriverPaymentComponent } from './driver/driver-payment/driver-payment.component';
import { AllPassengersComponent } from './all-passengers/all-passengers.component';
import { AddVehicleComponent } from './vehicle/add-vehicle/add-vehicle.component';
import { EditVehicleComponent } from './vehicle/edit-vehicle/edit-vehicle.component';
import { ViewAllVehicleComponent } from './vehicle/view-all-vehicle/view-all-vehicle.component';
import { AddFareComponent } from './fare-management/add-fare/add-fare.component';
import { FailListComponent } from './fare-management/fail-list/fail-list.component';
import { EditDriverComponent } from './driver/edit-driver/edit-driver.component';
import { AddHospitalComponent } from './hospital/add-hospital/add-hospital.component';
import { EditHospitalComponent } from './hospital/edit-hospital/edit-hospital.component';
import { AllHospitalComponent } from './hospital/all-hospital/all-hospital.component';
import { AllResponderComponent } from './responder/all-responder/all-responder.component';
import { ViewResponderComponent } from './responder/view-responder/view-responder.component';
import { AdminDashboardComponent } from './sub-admin/admin-dashboard/admin-dashboard.component';
import { AddSubAdminComponent } from './sub-admin/add-sub-admin/add-sub-admin.component';
import { AllSubAdminComponent } from './sub-admin/all-sub-admin/all-sub-admin.component';
import { AdminAccountComponent } from './sub-admin/admin-account/admin-account.component';
import { SubSideBarComponent } from './sub-admin/sub-side-bar/sub-side-bar.component';
import { SubHeaderComponent } from './sub-admin/sub-header/sub-header.component';
import { HospitalAccountComponent } from './hospital-admin/hospital-account/hospital-account.component';
import { HospitalPastBookingComponent } from './hospital-admin/hospital-past-booking/hospital-past-booking.component';
import { HospitalCurrentBookingComponent } from './hospital-admin/hospital-current-booking/hospital-current-booking.component';
import { AllBikeComponent } from './bike/all-bike/all-bike.component';


// export const MQTT_SERVICE_OPTIONS: IMqttServiceOptions = {
//   hostname: 'localhost',
//   port: 4201,
//   path: '/'
// }
@NgModule({
  declarations: [
    AppComponent,
    AccountComponent,
    DashboardComponent,
    HeaderComponent,
    SideBarComponent,
    ActiveTripComponent,
    CompleteTripComponent,
    BookedTripComponent,
    RouteMapComponent,
    TripSharedComponent,
    AddDriverComponent,
    AllDriverComponent,
    DriverPaymentComponent,
    AllPassengersComponent,
    AddVehicleComponent,
    EditVehicleComponent,
    ViewAllVehicleComponent,
    AddFareComponent,
    FailListComponent,
    EditDriverComponent,
    AddHospitalComponent,
    EditHospitalComponent,
    AllHospitalComponent,
    AllResponderComponent,
    ViewResponderComponent,
    AdminDashboardComponent,
    AddSubAdminComponent,
    AllSubAdminComponent,
    AdminAccountComponent,
    SubSideBarComponent,
    SubHeaderComponent,
    HospitalAccountComponent,
    HospitalPastBookingComponent,
    HospitalCurrentBookingComponent,
    AllBikeComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    MyDatePickerModule,
    NgSelectModule,
    NgZorroAntdModule,
    AgmCoreModule.forRoot({
      // apiKey: 'AIzaSyDvO4MiWWER38wQegvOy0VKk_WnNfBuf_Q',
      apiKey: 'AIzaSyDRVBkjjZkrZf-_blL06aGAeQ2uSCuJRn8',
      // libraries: ['geometry']
    }),
    AgmDirectionModule,
    // NgxMqttClientModule
    // Observable,
  //   NgxMqttClientModule.withOptions({
  //     // manageConnectionManually: true, //this flag will prevent the service to connection automatically
  //     host: 'http://localhost:4201/',
  //     // protocol: 'ws',
  //     port: 4201,
  //     path: '/'
  // }),
    // MqttModule.forRoot(MQTT_SERVICE_OPTIONS)
    MqttModule.forRoot(MQTT_SERVICE_OPTIONS)
  ],
  providers: [

  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
