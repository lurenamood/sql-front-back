import { useForm } from "react-hook-form";
import { useAxios } from "@hooks/useAxios";

export default function UserForm() {
    const {get, post} = useAxios()
  const {
    register,
    handleSubmit,
    formState: { errors, isSubmitting },
    reset,
  } = useForm();

  const onSubmit = async (data) => {
    try {
      await post('create_user', data);
      alert("Usuario creado");
      reset();
    } catch (error) {
      alert("Error al crear usuario");
      console.error(error);
    }
  };

  return (
    <form onSubmit={handleSubmit(onSubmit)} className="space-y-4">
      <input {...register("US_name", { required: true })} placeholder="Nombre" />
      {errors.name && <span>Nombre obligatorio</span>}

      <input {...register("US_surname", { required: true })} placeholder="Apellido" />
      {errors.surname && <span>Apellido obligatorio</span>}

      <input
        {...register("US_email", {
          required: true,
          pattern: {
            value: /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/,
            message: "Correo inválido",
          },
        })}
        placeholder="Correo"
      />
      {errors.email && <span>{errors.email.message || "Correo obligatorio"}</span>}

      <button type="submit" disabled={isSubmitting}>Guardar</button>
    </form>
  );
}
