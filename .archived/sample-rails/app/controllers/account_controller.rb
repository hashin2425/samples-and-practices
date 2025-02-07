class AccountController < ApplicationController
    def index
        @name = params[:name]
        @age = "MISSING"
        @user = AccountModel.find_by(name: @name)

        if @user
            @age = @user.age
        end

        render template: "account/index"
    end

    def annonimus
        render plain: "Hello, do you wanna create account?"
    end
end
