class Api::ExamplesController < ApplicationController
  def index
    examples = Example.all
    render json: examples
  end

  def create
    example = Example.new(example_params)
    if example.save
      render json: example, status: :created
    else
      render json: { errors: example.errors.full_messages }, status: :unprocessable_entity
    end
  end

  private

  def example_params
    params.require(:example).permit(:title)
  end
end
