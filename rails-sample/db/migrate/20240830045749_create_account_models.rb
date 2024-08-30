class CreateAccountModels < ActiveRecord::Migration[7.2]
  def change
    create_table :account_models do |t|
      t.text :name
      t.integer :age

      t.timestamps
    end
  end
end
