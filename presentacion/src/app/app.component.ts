import { Component } from '@angular/core';
import { PPService } from "./pp.service";
import { UserInsertService } from './create_user.service'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  nick_name=""
  description=""

  constructor(private userInsertService: UserInsertService){}

  public onSubmit(){
    const formData = new FormData();
    formData.append('nick_name', this.nick_name)
    formData.append('description', this.description)

    this.userInsertService.postFormData (formData).subscribe(
      (error)=>{
        console.log(error);
      },
      (sucess)=> {
        console.log(sucess);
      }
      );
  }


}
