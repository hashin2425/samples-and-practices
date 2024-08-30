class UsersController < ApplicationController
    def index
        @message = "Hello, world!"

        # /users?name=hoge-name
        @user_name = params[:name]

        render template: "users/index"
    end
end
