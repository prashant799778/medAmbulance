import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClient, HTTP_INTERCEPTORS }    from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MyDatePickerModule } from 'mydatepicker';
import { NgSelectModule } from '@ng-select/ng-select';
import { NgZorroAntdModule } from 'ng-zorro-antd';


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
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    MyDatePickerModule,
    NgSelectModule,
    NgZorroAntdModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
